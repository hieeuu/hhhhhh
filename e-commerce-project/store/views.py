# store/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, Address
from .forms import AddressForm
from django.views.generic import ListView

class BookListView(ListView):
    model = Book
    template_name = 'store/book_list.html' # Sẽ tạo ở phần frontend
    context_object_name = 'books'

# Xem danh sách địa chỉ của người dùng đã đăng nhập
@login_required
def address_list_view(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'store/address_list.html', {'addresses': addresses})

# Thêm địa chỉ mới
@login_required
def address_create_view(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('store:address_list')
    else:
        form = AddressForm()
    return render(request, 'store/address_form.html', {'form': form})

# Sửa địa chỉ
@login_required
def address_update_view(request, pk):
    address = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('store:address_list')
    else:
        form = AddressForm(instance=address)
    return render(request, 'store/address_form.html', {'form': form})

# Xóa địa chỉ
@login_required
def address_delete_view(request, pk):
    address = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == 'POST':
        address.delete()
        return redirect('store:address_list')
    return render(request, 'store/address_confirm_delete.html', {'address': address})

# Logic giả lập cho việc mua hàng
def checkout_view(request):
    # Nếu người dùng đã đăng nhập
    if request.user.is_authenticated:
        # Kiểm tra xem họ có địa chỉ nào chưa
        if not Address.objects.filter(user=request.user).exists():
            # Nếu chưa có, chuyển hướng đến trang thêm địa chỉ
            # Thêm một message để thông báo cho người dùng
            # from django.contrib import messages
            # messages.info(request, 'Vui lòng thêm địa chỉ giao hàng trước khi mua hàng.')
            return redirect('store:address_create')
        else:
            # Nếu đã có địa chỉ, tiến hành tới trang thanh toán (chúng ta sẽ làm sau)
            return render(request, 'store/payment.html')
    # Nếu là khách vãng lai
    else:
        # Chuyển hướng đến trang yêu cầu nhập thông tin giao hàng cho khách
        # Chúng ta sẽ xử lý logic này sau, có thể dùng session để lưu thông tin
        return render(request, 'store/guest_checkout_form.html')