from pynomo.nomographer import *

#Propofol dose

Prop_params={
    'u_min':10,
    'u_max':300,
    'function':lambda u:u,
    'title':r'$Propofol (mg)$',
    'tick_levels':3,
    'tick_text_levels':1,
    'tick_side':'left',

}

#target plasma concentration
Targ_params={
        'u_min':0.5,
        'u_max':8,
        'function':lambda u:u,
        'title':r'$Plasma Concentration$',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'left',
}

#weight, formula is for V1

Weight_params={
    'u_min':40,
    'u_max':100,
    'function':lambda u:u * 0.228,
    'title':r'$Weight (Kg)$',
    'tick_levels':3,
    'tick_text_levels':1,
    'tick_side':'left',
}

block_1_params={
    'block_type':'type_2',
    'width':10.0,
    'height':10.0,
    'f1_params':Prop_params,
    'f2_params':Tar_params,
    'f3_params':S_params,
}


main_params={
    'filename':'Type2-Example.pdf',
    'paper_height':10.0,
    'paper_width':10.0,
    'block_params':[block_1_params],
    'transformations':[('rotate',0.01),('scale paper',),('polygon',)],
    'title_x':5.0,
    'title_y':-1.0,
    'title_box_width': 10.0,
    'title_str':r'$(S+0.64)^{0.58}(0.74V) = P$'
}

Nomographer(main_params)
