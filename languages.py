import justpy as jp

levels = ['A1','A2','B1']
languages = ['🇫🇷','🇨🇳','🇲🇽']

def index():
    wp = jp.WebPage()
    container = jp.Div(classes="flex flex-col w-1/2 justify-center items-center m-auto",a=wp)
    jp.H2(text='Learn A New Language!',classes="text-5xl bold mb-3",a=container)
    
    jp.H2(text="Languages",classes='text-2xl',a=container)
    div_lang = jp.Div(classes="flex justify-center items-center",a=container)
    language_list = []
    for language in languages:
        label = jp.Label(classes='inline-block mb-1 p-1',a=div_lang)
        radio_btn = jp.Input(type='radio',name='language',value=language,a=label,
            btn_list=language_list)
        language_list.append(language)
        jp.Span(classes='ml-1',a=label,text=language)
        
    jp.H2(text="Level",classes='text-2xl',a=container)
    div_level = jp.Div(classes="flex justify-center items-center",a=container)
    level_list = []
    for level in levels:
        label = jp.Label(classes="inline-block mb-1 p-1",a=div_level)
        radio_btn = jp.Input(type='radio',name='level',value=level,a=label,
            btn_list=level_list)
        level_list.append(level)
        jp.Span(classes='ml-1 bold text-md',a=label,text=level)
    
    return wp

jp.justpy(index,port=8080)
