import json


class ABI2py:
    def __init__(self, abi_path, class_name=None, output_path=None, output_name=None):
        self.abi_path = abi_path
        self.indent = "    "
        self.func_noname_counter = (
            0  # count if functions have no name, not sure if this actually happens
        )
        self.class_name = (
            class_name  # name of the class you want, defaults to abi filename if None
        )
        self.output_name = (
            output_name  # name of output file, defaults to abi filename if None
        )
        # make sure you end output_path string with a /
        self.output_path = output_path  # the file path minus the file name
        # make the thing do the thing
        self._run()

    def _run(self):
        # Do the thing
        self._load_abi()
        txt = ""
        txt = txt + self._parse_class_header() + "\n"
        for item in self.abi:
            if item["type"] == "function":
                receipt = self._function_to_pyfunc(item)
                txt = txt + receipt
        # output to a .py
        if self.output_name == None:
            output_name = self.abi_path.split("/")[-1].split(".")[0]
        if self.output_path == None:
            output_path = ""
        else:
            output_path = self.output_path
        with open(output_path + output_name + ".py", "w+") as f:
            f.write(txt)

    def _load_abi(self):
        with open(self.abi_path) as f:
            self.abi = json.load(f)

    def _parse_class_header(self):
        # build the class header
        # give the abi self variable
        # allow web3 connection to be passed into class and make it self variable
        # use the name of the abi file as the class name if none is given
        if self.class_name == None:
            class_name = self.abi_path.split("/")[-1].split(".")[0]
        else:
            class_name = self.class_name
        head = (
            "class "
            + class_name
            + ":\n"
            + self.indent
            + "def __init__(self, web3_connection, addr):\n"
            + self.indent * 2
            + "self.web3 = web3_connection\n"
            + self.indent * 2
            + "self.addr = addr\n"
            + self.indent * 2
            + "self.abi = "
            + str(self.abi)
            + self.indent * 2
            + "\n"
            + self.indent * 2
            + "self.contract = self.web3.eth.contract(addr, abi=self.abi)"
        )
        return head

    def _function_to_pyfunc(
        self,
        abi_item,
    ):
        inputs = abi_item["inputs"]
        outputs = abi_item["outputs"]
        func_name = abi_item["name"]
        if func_name == "":  # catch if a function does not have a name
            func_name = "NONAME_" + str(self.func_noname_counter)
            self.func_noname_counter += 1
        input_line, input_for_output = self._parse_input(func_name, inputs)
        output_line = self._parse_output(func_name, input_for_output, outputs)
        input_docstr = self._parse_input_docstr(inputs)
        output_docstr = self._parse_output_docstr(func_name, outputs)
        txt = ""
        txt = (
            txt
            + "\n"
            + input_line
            + "\n"
            + self.indent * 2
            + '"""'
            + "\n"
            + input_docstr
            + "\n"
            + output_docstr
            + "\n"
            + self.indent * 2
            + '"""'
            + "\n"
            + output_line
            + "\n"
        )
        return txt

    def _parse_output(self, func_name, input_for_output, outputs):
        body = (
            self.indent * 2
            + "output = self.contract.functions."
            + func_name
            + "("
            + input_for_output
            + ").call()"
        )
        # body = body + "\n"
        name_counter = 0
        name_list = []  # store for later
        for output in outputs:
            name = output["name"]
            if name == "":
                name = func_name + "_OUTPUT_" + str(name_counter)
                name_list.append(name)
                name_counter += 1
        # if outputs is one item then it will only return a single output, not a list, there needs to be logic to handle that output, -- turn it into a list, instead of one single item
        if len(outputs) == 1:
            body = body + "\n"
            body = (
                body
                + self.indent * 2
                + "output_list = []\n"
                + self.indent * 2
                + "output_list.append(output)\n"
                + self.indent * 2
                + "output=output_list"
            )
        # make the output into a dictionary that is returned
        body = body + "\n" + self.indent * 2 + "output_dict={}"
        output_counter = 0
        name_list_counter = 0
        if name_list == []:  # if name_list is empty, then skip
            pass
        else:
            for output in outputs:
                body = body + "\n"
                # add in the variable as self and to a dict that is returned
                body = (
                    body
                    + self.indent * 2
                    + "self."
                    + name_list[name_list_counter]
                    + " = output["
                    + str(output_counter)
                    + "]"
                )
                body = body + "\n"
                body = (
                    body
                    + self.indent * 2
                    + 'output_dict["'
                    + name_list[name_list_counter]
                    + '"] = output['
                    + str(output_counter)
                    + "]"
                )
                output_counter += 1
                name_list_counter += 1
        body = body + "\n"
        body = body + self.indent * 2 + "return output_dict"
        body = body + "\n"
        return body

    def _parse_input(self, func_name, inputs):
        # parse input
        name_counter = 0
        input_for_output = (
            ""  # track inputs to make it easier to plug into self.parse_output
        )
        if inputs == []:
            input_line = self.indent + "def " + func_name + "(self):\n"
        else:
            input_line = self.indent + "def " + func_name + "(self"
            for input in inputs:
                name = input["name"]
                if name == "":
                    name = "INPUT_" + str(name_counter)
                    name_counter += 1
                input_for_output = input_for_output + name + ", "
                input_line = input_line + ", " + name
            input_line = input_line + "):"
        return input_line, input_for_output

    def _parse_input_docstr(self, inputs):
        # parse the inputs to look kind of nice in docstr
        txt = self.indent * 2 + "Args:\n"
        if inputs == []:
            txt = txt + self.indent * 3 + "None\n"
        else:
            for input in inputs:
                name = input["name"]
                name_counter = 0
                if name == "":
                    name = "INPUT_" + str(name_counter)
                    name_counter += 1
                input_type = input["type"]
                txt = txt + self.indent * 3 + name + " (" + input_type + ")\n"
        return txt

    def _parse_output_docstr(self, func_name, outputs):
        # parse the outputs to look kind of nice in docstr
        txt = self.indent * 2 + "Returns:\n"
        if outputs == []:
            txt = txt + self.indent * 3 + "None\n"
        else:
            for output in outputs:
                name = output["name"]
                name_counter = 0
                if name == "":
                    name = func_name + "_OUTPUT_" + str(name_counter)
                    name_counter += 1
                output_type = output["type"]
                txt = txt + self.indent * 3 + name + " (" + output_type + ")\n"
        return txt


if __name__ == "__main__":
    file = "DMM_POOL_ABI.json"
    abi = ABI2py(file)
    """
    abi._load_abi()
    txt = ""
    txt = txt + abi.parse_class_header() + "\n"
    for item in abi.abi:
        if item["type"] == "function":
            inp, outp = abi.function_to_pyfunc(item)
            txt = txt + "\n" + inp + "\n" + outp
    with open("abi_test.py", "w+") as f:
        f.write(txt)
    """
