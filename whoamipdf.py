
#
# PDF 파일  Happy load
#
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
# PDF 파일 경로
pdf_file_path = "whoami Gamma.pdf"

# PDF 뷰어 컴포넌트 사용
pdf_viewer(pdf_file_path)