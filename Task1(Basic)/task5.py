s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";


def rev(el):
    el = el.split(":")
    el.reverse()
    el = ":".join(el)
    return el


def res_el(el):
    return "("+el.replace(":", ", ")+")"


def s_transformation(string):
    string = sorted(list(map(rev, string.upper().split(";"))))
    string = " ".join(list(map(res_el, string)))
    return string


if __name__ == "__main__":
    print(s_transformation(s))
