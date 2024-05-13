#Charts were built on top of Plotly
#They accept Numpy and Dataframe objects 
#"marker" keyword argument which is a dictionary with the following arguments: size, color, symbol, opacity


from taipy import Gui

list_to_display= [3+x ** 2-2*x for x in range(1, 10)]
Gui("<|{list_to_display}|chart|>").run()