from django.urls import path
from . import views

urlpatterns = [
    path('', views.pos_page, name='pos'),   # ✅ FIXED HERE
    path('save-bill/', views.save_bill, name='save_bill'),
        # 🔥 HTML PAGE
    path('sales-report-page/', views.sales_report_page, name='sales_report_page'),

    # 🔥 API DATA
    path('sales-report/', views.sales_report, name='sales_report'),
    path('export-sales-excel/', views.export_sales_excel, name='export_sales_excel'),
    path("delete-today-sales/", views.delete_today_sales, name="delete_today_sales"),
    path("delete-all-sales/", views.delete_all_sales, name="delete_all_sales"),
    # ITEM
    path('items/', views.item_list, name='item_list'),
    path('items/add/', views.add_item, name='add_item'),
    path('items/edit/<int:pk>/', views.edit_item, name='edit_item'),
    path('items/delete/<int:pk>/', views.delete_item, name='delete_item'),

    

    path('category-list/', views.category_list, name='category_list'),

    path('add-category/', views.add_category, name='add_category'),

    path('edit-category/<int:pk>/', views.edit_category, name='edit_category'),

    path('delete-category/<int:pk>/', views.delete_category, name='delete_category'),

    path(
        'close-shift/',
        views.close_shift,
        name='close_shift'
    ),

    path(
        'edit-bill/<int:bill_id>/',
        views.edit_bill,
        name='edit_bill'
    ),

    path(
        'edited-bills/',
        views.edited_bills,
        name='edited_bills'
    ),

    # urls.py

    path(
        'edited-bill/<int:id>/',
        views.edited_bill_detail,
        name='edited_bill_detail'
    ),

    path(
        "verify-edit-bill/<int:bill_id>/",
        views.verify_edit_bill,
        name="verify_edit_bill"
    ),

    path(
        "bill-report/",
        views.bill_report,
        name="bill_report"
    ),

    path(
        "bill-detail/<int:bill_id>/",
        views.bill_detail,
        name="bill_detail"
    ),

    path(
        'delete-shift-sales/',
        views.delete_shift_sales,
        name='delete_shift_sales'
    ),
]