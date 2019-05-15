import habanero as ha


available_styles = ha.cn.csl_styles()
ref_string = ha.cn.content_negotiation(ids = "10.1126/science.169.3946.635", format = "text", style = "apa")
ref_string1 = ha.cn.content_negotiation(ids = "10.1126/science.169.3946.635", format = "text", style = "chicago-annotated-bibliography")
ref_string2 = ha.cn.content_negotiation(ids = "10.1126/science.169.3946.635", format = "text", style = "ieee")
print(ref_string)
print(ref_string1)
print(ref_string2)