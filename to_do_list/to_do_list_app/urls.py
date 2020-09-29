from django.urls import path

from . import views


app_name = "to_do_list_app"

urlpatterns = [

    path('', views.index_view, name="index_view"),
    path('add_data_view/', views.add_data_view, name='add_data_view'),
    path('delete_data_view/<int:delete_item_id>/', views.delete_data_view, name='delete_data_view'),
    path('update_data_view/<int:update_item_id>/', views.update_data_view, name='update_data_view'),

]
# path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete')
#path('delete_data_view/<int:todo_id>/', views.delete_data_view, name='delete_data_view'),
# path('delete_data_view/<int:delete_item_id>/', views.delete_data_view, name='delete_data_view'),
