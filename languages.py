import justpy as jp

levels = ['A1','A2','A3']
languages = ['🇫🇷','🇨🇳','🇲🇽']

def index():
    wp = jp.WebPage()
    div = jp.Div(classes="flex flex-col w-1/2 justify-center items-center m-auto",a=wp)
    jp.H2(text='Learn A New Language!',classes="text-5xl bold mb-3",a=div)
    
    jp.H2(text="Languages",classes='text-2xl',a=div)
    div_lang = jp.Div(classes="flex justify-center items-center",a=wp)
    language_list = []
    for language in languages:
        label = jp.Label(classes='inline-block mb-1 p-1',a=div_lang)
        radio_btn = jp.Input(type='radio',name='language',value=language,a=label,
            btn_list=language_list)
        language_list.append(language)
        jp.Span(classes='ml-1',a=label,text=language)
    
    return wp

jp.justpy(index,port=8080)
