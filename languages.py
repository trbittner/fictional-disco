import justpy as jp

levels = ['A1','A2','B1']
languages = [('🇫🇷','French'),('🇨🇳','Mandarin'),('🇲🇽','Mexican Spanish')]
media = ['Read','Listen']

story_params = dict.fromkeys(['levels','languages','media','tags'])

def radio_changed(self,msg):
    for btn in self.btn_list:
        if btn.checked:
            story_params[self.name] = btn.value

def create_radio_btn_group(src_list_name,is_text=True):
    div = jp.Div(classes='flex justify-center items-center')
    btn_list = []
    src_list = globals().get(src_list_name)
    for item in src_list:
        val = item
        classes = 'ml-1'
        if is_text:
            classes += ' bold text-md'
        else:
            val = item[1]
        label = jp.Label(classes='inline-block mb-1 p-1',a=div)
        radio_btn = jp.Input(type='radio',name=src_list_name,value=val,a=label,
        btn_list=btn_list,change=radio_changed)
        btn_list.append(radio_btn)

        jp.Span(classes='ml-1',a=label,text=item)
        
    return div
    
def get_params(self,msg):
    tags = self.input.value.split(' ')[:5]
    story_params['tags'] = tags
    print(story_params)

def index():
    wp = jp.WebPage()
    container = jp.Div(classes="flex flex-col w-1/2 justify-center items-center m-auto",a=wp)
    jp.H2(text='Learn A New Language!',classes="text-5xl bold mb-3",a=container)
    
    jp.H2(text="Languages",classes='text-2xl',a=container)
    container.add(create_radio_btn_group('languages',False))

    jp.H2(text="Level",classes='text-2xl',a=container)
    container.add(create_radio_btn_group('levels'))
        
    jp.H2(text='I want to...',classes='text-2xl',a=container)
    container.add(create_radio_btn_group('media'))
    
    input = jp.Input(placeholder = 'Add up to 5 tags to facilitate story creation...',
        classes='focus:outline-none border border-gray-300 p-1 mr-2 mb-2 w-11/12 \
        shadow-lg rounded-md',a=container)
    
    go_btn = jp.Button(text='Go',classes='bg-gray-200 p-2 rounded mb-4',a=container)
    go_btn.on('click',get_params)
    go_btn.input = input
    
    jp.Div(classes="flex justify-right")
    
    return wp

jp.justpy(index,port=8080)
