class Locators:
    #HomePage
    homePage_SearchBar_XPATH = "//header/nav[@id='navbar']/div[1]/div[3]/div[2]/form[1]/div[1]/div[1]/input[1]"
    homePage_Cart_XPATH= "//span[contains(text(),'Carrito')]"
    homePage_searchButton_XPATH="//header/nav[@id='navbar']/div[1]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/button[1]/span[1]"

    #ProductPage
    product_selectedProduct_XPATH= "//body/div[3]/main[1]/div[1]/div[7]/div[2]/div[1]/div[1]/a[1]/div[1]/figure[1]/picture[1]/img[1]"
    product_addToCart_XPATH="//button[@id='buy-now']"
    product_addToCartConfirmation_XPATH="//a[contains(text(),'Ir al carrito')]"

    #Cart
    cart_eliminarProducto_XPATH = "//a[contains(text(),'Eliminar')]"
    cart_productoVerificado_XPATH = "(//a[@href='/p/iphone-12-64gb-negro--qepsn7'])[2]"