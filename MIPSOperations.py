
def handle_condition(self ,var1, var2, operator :str) -> str:
    string :str = ""
    if operator   == "==":
        string = "beq $t0, $t1, then"
    elif operator == "!=":
        string = "bne $t0, $t1, then"
    elif operator == "<":
        string = "blt $t0, $t1, then"
    elif operator == ">":
        string = "bgt $t0, $t1, then"
    elif operator == "<=":
        string = "ble $t0, $t1, then"
    elif operator == ">=":
        string = "bge $t0, $t1, then"
    else:
        print("error")

    return string


def handle_condition_if(operator:str, label:str) -> list[str]:
        # Assumes the condition variables, are in $t0 and $t1
        # For an If loop, we need to reverse the condition
        string:str = ""

        if operator   == "==":
            string = "bne $t0, $t1, " + label
        elif operator == "!=":
            string = "beq $t0, $t1, " + label
        elif operator == "<":
            string = "bge $t0, $t1, " + label
        elif operator == ">":
            string = "ble $t0, $t1, " + label
        elif operator == "<=":
            string = "bgt $t0, $t1, " + label
        elif operator == ">=":
            string = "blt $t0, $t1, " + label
        else:
            print("error")

        return [string]