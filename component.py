import streamlit as st

name = st.text_input("请输入你的名字：")
if name:
    st.write(f'你好,{name}')

column1, column2, column3 = st.columns(3)
with column1:
    password = st.text_input("请输入你的密码:", type='password')

with column2:
    paragraph = st.text_area('请输入一段自我介绍：')

with column3:
    age = st.number_input('请输入你的年龄：', value=20, min_value=0, max_value=150, step=1)
    st.write(f'你的年龄是：{age}岁')

st.divider()
checked = st.checkbox('同意以上条款：')
if checked:
    st.write('感谢你的同意！')

st.divider()
submitted = st.button('提交')
if submitted:
    st.write('提交成功！')

tab1, tab2, tab3 = st.tabs(['性别','联系方式','喜好水果'])
with tab1:
    gender = st.radio('你的性别是什么？',
         ['男性','女性','跨性别'],
         index=None)
    if gender:
        st.write(f'你选择的性别是{gender}')

with tab2:
    contact = st.selectbox('你希望通过什么方式联系？',
                 ['电话','邮件','微信','QQ','其他'])
    st.write(f'好的，我们会通过{contact}联系你')

with tab3:
    fruits = st.multiselect('你喜欢的水果是什么？',
                   ['苹果','香蕉','橙子','梨','西瓜','葡萄'])
    for fruit in fruits:
        st.write(f'你选择的水果是{fruit}')

with st.expander('身高信息'):
    height = st.slider('你的身高是多少厘米？',value=170,
          min_value=100, max_value=230,step=1)

st.divider()
uploaded_file = st.file_uploader('上传文件',type=['png','jpg','jpeg'])
if uploaded_file:
    st.write(f'你上传的文件是{uploaded_file.name}')
    st.write(f'文件内容如下：{uploaded_file.read()}')

# 侧边栏
with st.sidebar:
    user_name = st.text_input('用户名字是:')




