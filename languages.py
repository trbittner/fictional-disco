import justpy as jp

levels = ['A1','A2','B1']
languages = ['🇫🇷','🇨🇳','🇲🇽']
stories = ['Read','Listen']

def create_radio_btn_group(src_list_name,is_text=True):
    div = jp.Div(classes='flex justify-center items-center')
    
    btn_list = []
    src_list = globals().get(src_list_name)
    for item in src_list:
        label = jp.Label(classes='inline-block mb-1 p-1',a=div)
        jp.Input(type='radio',name=src_list_name,value=item,a=label,
        btn_list=btn_list)
        btn_list.append(item)
        classes = 'ml-1'
        if is_text:
            classes += ' bold text-md'
        jp.Span(classes='ml-1',a=label,text=item)
        
    return div

def index():
    wp = jp.WebPage()
    container = jp.Div(classes="flex flex-col w-1/2 justify-center items-center m-auto",a=wp)
    jp.H2(text='Learn A New Language!',classes="text-5xl bold mb-3",a=container)
    
    jp.H2(text="Languages",classes='text-2xl',a=container)
    container.add(create_radio_btn_group('languages',False))

    jp.H2(text="Level",classes='text-2xl',a=container)
    container.add(create_radio_btn_group('levels'))
        
    jp.H2(text='I want to...',classes='text-2xl',a=container)
    container.add(create_radio_btn_group('stories'))
    
    jp.Input(placeholder = 'Add up to 5 tags to facilitate story creation...',
    classes='focus:outline-none border border-gray-300 p-1 mr-2 mb-2 w-11/12 \
        shadow-lg rounded-md',a=container)
    
    jp.Button(text='Go',classes='bg-gray-200 p-2 rounded',a=container)
    

    
    return wp

jp.justpy(index,port=8080)
