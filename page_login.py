# -*- coding: utf-8 -*-
"""登录页面"""

import streamlit as st
from auth_mod import do_login, is_logged_in


def render():
    if is_logged_in():
        return

    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.markdown("###  登录 NORVIK SHOP")
        st.caption("企业级跨境电商 AI 运营系统")

        with st.form("login_form"):
            username = st.text_input("账号", placeholder="请输入用户名")
            password = st.text_input("密码", type="password", placeholder="请输入密码")
            submitted = st.form_submit_button("  登录", use_container_width=True)

            if submitted:
                if not username or not password:
                    st.warning("请输入账号和密码")
                elif do_login(username, password):
                    st.success("登录成功，正在跳转…")
                    st.rerun()
                else:
                    st.error("账号或密码错误，或账号已被锁定")

        st.caption("默认管理员: admin / admin123")
