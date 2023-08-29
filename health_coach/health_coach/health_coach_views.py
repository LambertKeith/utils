import streamlit as st

from health_coach.views_utils import calculate_bmi, interpret_bmi

def main():
    st.set_page_config(page_title="health_coach 界面", page_icon="🌟")
    st.title("health_coach Streamlit 界面")
    st.write("这是一个简单的Streamlit界面。")
    BMI_input_part()


    


def BMI_input_part():
    '''
    BMI体重界面
    '''
    height_col, weight_col = st.columns(2)
    height = height_col.text_input('身高(m)')
    weight = weight_col.text_input('体重(kg)')

    get_bmi = st.button('计算')
    if get_bmi and height != '' and weight != '':
        #计算bmi
        bmi = calculate_bmi(eval(weight), eval(height))
        st.info(bmi)
        st.info(interpret_bmi(bmi))
        
    else:
        st.info('请输入必要的数值')
