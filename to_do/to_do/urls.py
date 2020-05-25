"""to_do URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_defined_in_view, name="index_i_will_use_in_html"),
    path('new_url', views.new_defined_in_view, name="new_i_will_use_in_html"),
    path('detail_url/<int:pk_i_clicked>', views.detail_defined_in_view, name="detail_i_will_use_in_html"),
    # path('coding_url', views.coding_in_view, name='coding_i_will_use_in_html'),
    # path('toefle_url', views.toefle_in_view, name='toefle_i_will_use_in_html'),
    # path('excel_url', views.excel_in_view, name='excel_i_will_use_in_html'),
    path('edit_url/<int:pk_i_clicked>', views.edit_defined_in_view, name="edit_i_will_use_in_html"),
    path('delete_url/<int:pk_i_clicked>', views.delete_defined_in_view, name="delete_i_will_use_in_html"),
    path('delete_comment/<int:article_pk>/<int:comment_pk>',views.delete_comment, name="delete_comment")
]

# ★★ 질문 ★★
# ㅡ coding, toefle, excel을 눌러야 detail로 가지는거 아닌가. 왜 url path가 필요없지? 
# 저번과는 달리 따로 보이는게 아니라...detail로 다 묶여져 있는...?

# 맨 마지막에서 article_pk .....
# Question : delte_comment 에 필요한 url은 한 번에 어떻게 생각해내는지? 