Msigana ecommerce
python -m django --version
pip freeze > requirements.txt

python manage.py makemigrations --dry-run --verbosity 3




# Import the necessary models
from store.models import Product, SizeVariation, Variation, Color

# Get the last product
last_product = Product.objects.last()

# Get the size variations of the last product
size_variations = SizeVariation.objects.filter(product=last_product)

# For each size variation, get the variations and their colors
for size_variation in size_variations:
    print(f"Product Name: {last_product.product_name}")
    print(f"Size: {size_variation.size.name}")
    print(f"Price: {size_variation.price}")
    variations = Variation.objects.filter(size_variation=size_variation)
    for variation in variations:
        colors = Color.objects.filter(variation=variation)
        for color in colors:
            print(f"Color: {color.name}")
    print("\n")





    {% extends 'base.html' %}
{% load static %}
{% load socialaccount %}

{% block content %}
<style>
    input[type="radio"]:checked + .size-label,
    input[type="radio"]:checked + .color-label {
        background-color: pink;
    }
</style>

    <div class="py-4 container flex gap-3 items-center px-4 sm:px-8 md:px-16 lg:px-32 xl:px-32 2xl:max-w-9xl 2xl:mx-auto">
        <a href="{% url 'home' %}" class="text-primary text-base font-medium uppercase">
            <i class="fas fa-home"></i>
        </a>
        <span class="text-sm text-gray-400"><i class="fas fa-chevron-right"></i></span>
        <a href="{{single_product.category.get_url}}" class="text-primary text-base font-medium uppercase">
            {{single_product.category}}
        </a>
        <span class="text-sm text-gray-400"><i class="fas fa-chevron-right"></i></span>
        <p class="text-blue-600 font-medium uppercase " style="white-space: nowrap;">{{single_product.product_name}}</p>
    </div>
    <div class="container pt-4 pb-6 grid lg:grid-cols-2 gap-6 items-center px-4 sm:px-8 md:px-16 lg:px-32 xl:px-32 2xl:max-w-9xl 2xl:mx-auto">
        <div>
            <div>
                <div style="position: relative; text-align: center;">
                    <img id="main-img" src="{{ main_image.image.url }}" class="w-full h-64 lg:h-[340px] xl:h-[390px] 2xl:h-[420px]">
                    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 30px; font-weight: 300; color: silver; font-family: 'Pacifico', cursive;">
                        <i class="fas fa-star"></i> Tanabeles
                    </div>
                    <div class="flex justify-end absolute bottom-2 right-2 space-x-2">

                        <!-- Share button -->
                        <div class="mr-2 md:mr-4">
                            <div class="w-14 h-14 bg-slate-600 rounded-full flex items-center justify-center">
                                <button onclick="shareProduct()">
                                    <i class="fas fa-share-alt text-white text-2xl"></i>
                                </button>
                            </div>
                        </div>
        
                        <!-- Heart button -->
{% load socialaccount %}
<div>
    <div id="product-container" class="w-14 h-14 text-white rounded-full flex items-center justify-center {% if liked %} bg-red-500 {% else %} bg-slate-600 {% endif %}">
        {% if user.is_authenticated %}
        <button id="like-button" class="like-button" data-product-slug="{{ single_product.product_slug }}" data-liked="{{ liked|lower }}">
            <i id="heart-icon" class="fas fa-heart text-2xl"></i>
        </button>
        {% else %}
        <a id="like-button" href="/accounts/login/">
            <i id="heart-icon" class="fas fa-heart text-2xl"></i>
        </a>
        {% endif %}
    </div>
</div>
        
                    </div>
                </div>
                <div class="grid grid-cols-5 gap-4 mt-4">
                    {% for image in other_images %}
                        <div>
                            <img src="{{ image.image.url }}" class="single-img w-full h-12 md:h-16 xl:h-20 cursor-pointer border rounded-lg object-cove">
                        </div>
                    {% endfor %}
                </div>
            </div> 
        </div>
        <!-- product image end -->
        <!-- product content -->
        <div>
            
            <h2 class="md:text-3xl text-2xl font-medium uppercase mb-2">{{single_product.product_name}}</h2>
            <div class="flex flex-col-2 gap-4">
                <div class="w-1/2">
                    <span class="flex items-center">
                        <span>{{ single_product.product_owner.first_name | capfirst }}</span>
                        <img class="h-8 ml-1" src="{% static 'images/verified-badge.png' %}" alt="Verified Badge">
                      </span>
                      
            <div class="space-y-1">
                <p class="text-sm md:text-base text-gray-800 font-semibold space-x-2">
                    <span>Availability: </span>
                    {% if single_product.product_stock <= 0 %}

                    <span class="text-sm md:text-base text-red-600">out of stock</span>
                    {% else %}
                     <span class="text-sm md:text-base text-green-600">In Stock</span>
                    {% endif %}
                </p>
                <p class="space-x-2">
                    <span class="text-sm md:text-base text-gray-800 font-semibold">Brand: </span>
                    <span class="text-sm md:text-base text-gray-600">{{single_product.product_brand|capfirst}}</span>
                </p>
                <p class="space-x-2">
                    <span class="text-sm md:text-base text-gray-800 font-semibold">Category: </span>
                    <span class="text-sm md:text-base text-gray-600">{{single_product.category|capfirst}}</span>
                </p>
                <p class="space-x-0 md:space-x-2">
                    
                    <span class="text-sm md:text-base text-gray-800 font-semibold">Price: </span>
                    {% load price_filters %}
                {% comment %} <span class="text-sm md:text-base text-primary font-semibold">{{single_product.product_price|discounted_price}} birr</span> {% endcomment %}
                <span id="product-price" class="text-gray-500 text-base line-through">Loading ... birr</span>
                </p>
            </div>
        </div>
        <div class="w-1/2">
            
            
            <div class="flex items-center mb-0 md:mb-4">
                
                <div class="flex gap-1 text-xs md:text-sm text-yellow-400">
                    <span><i class="fas fa-star"></i></span>
                    <span><i class="fas fa-star"></i></span>
                    <span><i class="fas fa-star"></i></span>
                    <span><i class="fas fa-star"></i></span>
                    <span><i class="fas fa-star"></i></span>
                </div>
                <div class="text-xs text-gray-500 ml-3">(150 Reviews)</div>
            </div>
            <div class="flex items-center">
                <svg class="h-4 md:h-6" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M288 80c-65.2 0-118.8 29.6-159.9 67.7C89.6 183.5 63 226 49.4 256c13.6 30 40.2 72.5 78.6 108.3C169.2 402.4 222.8 432 288 432s118.8-29.6 159.9-67.7C486.4 328.5 513 286 526.6 256c-13.6-30-40.2-72.5-78.6-108.3C406.8 109.6 353.2 80 288 80zM95.4 112.6C142.5 68.8 207.2 32 288 32s145.5 36.8 192.6 80.6c46.8 43.5 78.1 95.4 93 131.1c3.3 7.9 3.3 16.7 0 24.6c-14.9 35.7-46.2 87.7-93 131.1C433.5 443.2 368.8 480 288 480s-145.5-36.8-192.6-80.6C48.6 356 17.3 304 2.5 268.3c-3.3-7.9-3.3-16.7 0-24.6C17.3 208 48.6 156 95.4 112.6zM288 336c44.2 0 80-35.8 80-80s-35.8-80-80-80c-.7 0-1.3 0-2 0c1.3 5.1 2 10.5 2 16c0 35.3-28.7 64-64 64c-5.5 0-10.9-.7-16-2c0 .7 0 1.3 0 2c0 44.2 35.8 80 80 80zm0-208a128 128 0 1 1 0 256 128 128 0 1 1 0-256z"/></svg>
                <span class="ml-2 text-gray-600">{{ single_product.product_views_count }} Views</span>
            </div>       
{% if size_variations %}
<div class="mt-2 md:mt-4">
    <h3 class="text-sm md:text-base text-gray-800 font-semibold mb-1">Size</h3>
    <div class="flex flex-row flex-wrap items-center gap-2">
        <!-- single size -->
        {% for variation in size_variations %}
    <div class="size-selector">
        <input type="radio" name="size" class="hidden size-radio" id="size-{{ variation.size.name|lower }}" value="{{ variation.size.name|lower }}" data-id="{{ variation.id }}" {% if forloop.first %}checked{% endif %}>
        <label for="size-{{ variation.size.name|lower }}"
            class="size-label text-sm md:text-base border border-gray-200 rounded-sm h-6 md:h-8 px-1 md:px-2 flex items-center justify-center cursor-pointer shadow-sm text-gray-600">
            {{ variation.size.name|capfirst }}
        </label>
    </div>
{% endfor %}
    </div>
</div>
{% endif %}
<!-- size end -->


<!-- color -->

<div class="mt-4">
    <h3 class="text-sm md:text-base text-gray-800 font-semibold mb-1">Color</h3>
    <div id="color-container" class="flex items-center gap-2">
        <!-- Color radio buttons will be inserted here by JavaScript -->
    </div>
</div>

<script>
   $(document).ready(function() {
    var prices = {};
    var colors = {};

    $('.size-radio').each(function() {
        var variationId = $(this).data('id');
        $.ajax({
            url: '/store/get_price_and_colors/',
            data: {
                'variation_id': variationId
            },
            dataType: 'json',
            success: function (data) {
                console.log('Price fetched:', data.price);
                console.log('Colors fetched:', data.colors);
                prices[variationId] = data.price;
                colors[variationId] = data.colors;

                if ($('.size-radio:checked').data('id') === variationId) {
                    $('#product-price').text(data.price + ' birr');
                    updateColors(data.colors);
                    $('#selected-price').val(data.price);
                }
            }
        });
    });

    $('input[name="color"]').each(function() {
        console.log('Color input:', this, 'ID:', this.id, 'Parent:', $(this).parent());
    });
    
    $('.size-radio').change(function() {
        var variationId = $(this).data('id');
        console.log('Size changed:', variationId, prices[variationId]);
        $('#product-price').text(prices[variationId] + ' birr');
        updateColors(colors[variationId]);
        $('#selected-price').val(prices[variationId]);
    });

    function updateColors(colorList) {
        // Remove existing color radio buttons
        $('.color-selector').remove();
    
        // Generate new color radio buttons
        colorList.forEach(function(color, index) {
            var colorSelector = $('<div class="color-selector"></div>');
            var colorInput = $('<input type="radio" name="color" class="hidden" id="color-' + color.toLowerCase() + '">');
            if (index === 0) {
                colorInput.prop('checked', true);
            }
            var colorLabel = $('<label for="color-' + color.toLowerCase() + '" class="color-label text-xs rounded-sm h-5 w-5 flex items-center justify-center cursor-pointer shadow-sm">' + color.charAt(0).toUpperCase() + color.slice(1).toLowerCase() + '</label>');
            colorSelector.append(colorInput);
            colorSelector.append(colorLabel);
            $('#color-container').append(colorSelector); // Change this line
        });
    }
});
</script>




{% comment %} <script>
    $(document).ready(function() {
        // Fetch all prices when the page loads
        var prices = {};
        $('.size-radio').each(function() {
            var variationId = $(this).data('id');
            $.ajax({
                url: '/store/get_price/',
                data: {
                    'variation_id': variationId
                },
                dataType: 'json',
                success: function (data) {
                    console.log('Price fetched:', data.price);
                    prices[variationId] = data.price;
                    // If this is the initially selected size, update the displayed price
                    if ($('.size-radio:checked').data('id') === variationId) {
                        $('#product-price').text(data.price + ' birr');
                        // Update the value of the hidden input field
                        $('#selected-price').val(data.price);
                    }
                }
            });
        });

        // Update the displayed price when the selected size changes
        $('.size-radio').change(function() {
            var variationId = $(this).data('id');
            console.log('Size changed:', variationId, prices[variationId]);
            $('#product-price').text(prices[variationId] + ' birr');
            // Update the value of the hidden input field
            $('#selected-price').val(prices[variationId]);
        });
    });
</script> {% endcomment %}
</div>
</div> 
            <!-- add to cart button -->
            <div class="flex gap-3 border-b border-gray-200 pb-5 mt-6">
                {% if single_product.product_stock <= 0 %}

                <span class="text">out of stock</span>
                {% else %}
                <form action="{% url 'add_cart' single_product.id %}" method="POST">
                    {% csrf_token %}
                    <input type="hidden" name="product_name" value="{{ single_product.product_name }}">
                    <input type="hidden" id="selected-price" name="selected_price" value="">

                <button type="submit" class="bg-blue-700 border border-primary text-white px-3 xl:px-8 py-2 font-medium rounded uppercase 
                hover:bg-pink-500 hover:text-primary transition text-sm flex items-center">
                <span class="mr-2"><i class="fas fa-shopping-bag"></i></span> Add to cart
            </button>
            </form>
                {% endif %}
                <a href="tel:{{single_product.product_phone}}" class="bg-red-600 border border-gray-300 text-white px-3 xl:px-8 py-2 font-medium rounded uppercase 
                text-sm flex items-center">
                <span class="mr-1 xl:mr-2 text-blue-500 text-lg">
                    <svg xmlns="http://www.w3.org/2000/svg" height="16" width="16" viewBox="0 0 512 512">
                        <!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2023 Fonticons, Inc.-->
                        <path d="M164.9 24.6c-7.7-18.6-28-28.5-47.4-23.2l-88 24C12.1 30.2 0 46 0 64C0 311.4 200.6 512 448 512c18 0 33.8-12.1 38.6-29.5l24-88c5.3-19.4-4.6-39.7-23.2-47.4l-96-40c-16.3-6.8-35.2-2.1-46.3 11.6L304.7 368C234.3 334.7 177.3 277.7 144 207.3L193.3 167c13.7-11.2 18.4-30 11.6-46.3l-40-96z"/>
                    </svg>
                </span>
                <span class="text-base md:text-base xl:text-lg">{{single_product.product_phone|slice:":2"}}-{{single_product.product_phone|slice:"2:4"}}-{{single_product.product_phone|slice:"4:6"}}-{{single_product.product_phone|slice:"6:8"}}-{{single_product.product_phone|slice:"8:"}}</span>
            </a>
            </div>
            <div class="flex space-x-3 mt-4">
                <a href="{{ single_product.product_owner.facebook_url }}" target="_blank"
                    class="bg-amber-200 h-8 w-8 rounded-full border border-gray-300 flex items-center justify-center">
                    <i class="fab fa-facebook-f text-blue-600"></i>
                </a>
                <a href="{{ single_product.product_owner.telegram_url }}" target="_blank"
                    class="bg-amber-200 h-8 w-8 rounded-full border border-gray-300 flex items-center justify-center">
                    <i class="fab fa-telegram text-blue-600"></i>
                </a>
                <a href="{{ single_product.product_owner.whatsapp_url }}" target="_blank"
                    class="bg-amber-200 h-8 w-8 rounded-full border border-gray-300 flex items-center justify-center">
                    <i class="fab fa-whatsapp text-xl text-bold text-green-700"></i>
                </a>
            </div>
        </div>
    </div>
    <div class="container pb-8 items-center px-4 sm:px-8 md:px-16 lg:px-32 xl:px-32 2xl:max-w-9xl 2xl:mx-auto">
        <h3 class="border-b border-gray-200 font-roboto text-gray-800 pb-3 font-medium">
            Product Details
        </h3>
        <div class="lg:w-4/5 xl:w-3/5 pt-6">
                <p>
                    {{single_product.product_description}}
                </p>
        </div>
    </div>
    {% if related_products %}
    <div class="container pb-8 items-center px-4 sm:px-8 md:px-16 lg:px-32 xl:px-32 2xl:max-w-9xl 2xl:mx-auto">
        <h2 class="text-2xl md:text-3xl font-medium text-gray-800 uppercase mb-6">related products</h2>
        <div class="grid grid-cols-2 lg:grid-cols-4 sm:grid-cols-2 gap-6">
            {% for product in related_products %}
                <div class="group rounded bg-white shadow overflow-hidden">
                    <div class="w-full h-32 2xl:h-64 overflow-hidden relative">
                        <img src="{{ product.get_main_image.image.url }}" class="w-full">
                    </div>
                    <div class="pt-4 pb-3 pl-2  md:px-4 ">
                        <a href="{% url 'product_detail' product.category.category_slug product.product_slug %}">
                            <h4 class="uppercase font-medium text-base lg:text-sm  xl:text-lg mb-2 text-gray-800 hover:text-primary transition">
                                {{ product.get_short_name|capfirst }}
                            </h4>
                        </a>
                        <div class="my-0 2xl:my-2 text-blue-600 text-sm md:text-base">
                            {% load price_filters%}
                            {{ product.product_price|discounted_price }}br
                            <span class="text-gray-500 text-base line-through">{{ product.product_price }}br</span>
                        </div>
                        <!-- Add your product rating and reviews here -->
                    </div>
                    <!-- product content end -->
                    <!-- product button -->
                    <a href="{% url 'product_detail' product.category.category_slug product.product_slug %}"
                        class="block w-full py-1 text-center text-white bg-blue-600 border border-primary rounded-b hover:bg-blue-300 hover:text-primary transition">
                        Product details
                    </a>
                    <!-- product button end -->
                </div>
                <!-- single product end -->
            {% endfor %}
        </div>
    </div>
    {% endif %}
    <!-- related products end -->
<!-- Heart button -->





 
<script>
    document.addEventListener('DOMContentLoaded', function() {
        var viewedProducts = JSON.parse(localStorage.getItem('viewedProducts')) || {};
    
        console.log('viewedProducts:', viewedProducts);
    
        if (!viewedProducts['{{ single_product.product_slug }}']) {
            console.log('Product not viewed before, making fetch request');
            viewedProducts['{{ single_product.product_slug }}'] = true;
            localStorage.setItem('viewedProducts', JSON.stringify(viewedProducts));
    
            // Increment the view count
            fetch('/increment-view-count/{{ single_product.product_slug }}/', { 
                method: 'POST',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}',
                    'Content-Type': 'application/json'
                }
            }).then(response => {
                console.log('Fetch response:', response);
            }).catch(error => {
                console.log('Fetch error:', error);
            });
        }
    });
</script> 


 <script>
    $(document).ready(function () {
        const likeButton = $('#like-button');
        const heartIcon = $('#heart-icon');
        const productContainer = $('#product-container');
        const isAuthenticated = '{{ user.is_authenticated }}' === 'True';
        const url = '/store/product/' + likeButton.data('productSlug') + '/like/';
    
        likeButton.on('click', function (event) {
            event.preventDefault();
    
            if (!isAuthenticated) {
                window.location.href = '/accounts/login/';
                return;
            }
    
            $.ajax({
                url: url,
                type: 'POST',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}',
                },
                dataType: 'json',
                success: function (data) {
                    if (data.liked) {
                        productContainer.removeClass('bg-slate-600').addClass('bg-red-500');
                    } else {
                        productContainer.removeClass('bg-red-500').addClass('bg-slate-500');
                    }
                },
                error: function (xhr, textStatus, errorThrown) {
                    console.error('Error:', errorThrown);
                },
            });
        });
    });
</script> 

 <script>
    function shareProduct() {
        const productName = "{{ single_product.product_name }}";
        const categorySlug = "{{ single_product.category.get_url }}";
        const productSlug = "{{ single_product.product_slug }}";

        const productUrl = `https://tanabeles.com/store/${categorySlug}/${productSlug}`;

        if (navigator.share) {
            navigator.share({
                title: productName,
                text: `Check out this product: ${productName}`,
                url: productUrl,
            })
            .then(() => console.log('Shared successfully'))
            .catch((error) => console.error('Error sharing:', error));
        } else {
            // Fallback for browsers that do not support the Share API
            alert(`Share this products: ${productName}\n${productUrl}`);
        }
    }
</script> 
 <script>
    let mainImg = document.getElementById('main-img')
    let imgBars = document.getElementsByClassName('single-img')

    for(let imgBar of imgBars){
        imgBar.addEventListener('click', function(){
            clearActive()
            let imgPath = this.getAttribute('src')
            mainImg.setAttribute('src', imgPath)
            this.classList.add('border-green-600')
        })
    }

    function clearActive(){
        for(let imgBar of imgBars){
            imgBar.classList.remove('border-green-600')
        }
    }
</script> 
    <div class=" items-center px-4 sm:px-8 md:px-16 lg:px-32 xl:px-32 2xl:max-w-9xl 2xl:mx-auto mb-4">
        <a href="{% url 'home' %}" class="inline-block bg-green-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors duration-200">
            <i class="fas fa-arrow-left"></i> Back to shop
        </a>
        </div>
    


   
{% endblock %}





import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Use the JSON key you downloaded when creating your Google Cloud project
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/json/keyfile', scope)
client = gspread.authorize(creds)

# Open the Google Sheets document and get the first sheet
sheet = client.open('name_of_your_google_sheet').sheet1

# Write some data to the sheet
sheet.append_row(['first_name', 'last_name', 'order_phone', 'order_email', 'order_date', 'order_total_prices', 'order_address', 'payment_status', 'status'])

from .models import Order
orders = Order.objects.all()
for order in orders:
    sheet.append_row([order.first_name, order.last_name, order.order_phone, order.order_email, order.order_date, order.order_total_prices, order.order_address, order.payment_status, order.status])










































<div class="container pt-4 pb-6  gap-6 items-center px-4 sm:px-8 md:px-16 lg:px-32 xl:px-32 2xl:max-w-9xl 2xl:mx-auto">
    <div class="py-4 container flex gap-3 items-center">
        <a href="{% url 'home' %}" class="text-primary text-base">
            <i class="fas fa-home"></i>
        </a>
        <span class="text-sm text-gray-400"><i class="fas fa-chevron-right"></i></span>
        <p class="text-gray-600 font-medium uppercase">My Account</p>
    </div>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save changes</button>
    </form>
    <p>Username: {{ user.first_name }}</p>

    <h2>Liked products:</h2>
    <ul>
        {% for product in liked_products %}
            <li>{{ product.product_name }}</li>
            <img src="{{ product.get_main_image.image.url }}" alt="{{ product.product_name }}">
        {% empty %}
            <li>No liked products</li>
        {% endfor %}
    </ul>













     <div class="space-y-1 pl-8 shadow ">
                           <a href="account.html" 
                               class="relative text-sm md:text-base font-medium capitalize h transition block text-black pl-4">
                                   Customer Email
                               <span class="absolute -left-8 top-0 text-base px-4 text-green-600">
                                   <i class="far fa-address-card sm:hidden md:block"></i>
                               </span>
                           </a>
                           <a href="profile-info.html" class=" txt-sm block pl-4">{{user.email}}</a>
                       </div>