(function() {
    console.log("nikestore.js");
    var timeInterval = 100; // milliseconds

    var waitForPage = window.setInterval(function() { waitForPageToLoad() }, 10);

    function waitForPageToLoad() {
        var addToCartDiv = document.getElementsByClassName("add-to-cart")[0];
        
        if (isValidVariable(addToCartDiv)) {
            window.clearInterval(waitForPage);
            console.log("page loaded");
            pickShoeSize();
            addToCartSetup();
        }
    }

    function pickShoeSize() {
        var sizePriority = ["12", "11.5", "12.5", "11", "13", "10.5", "13.5", "10", "14", "9.5", "9"];
        var sizesAvailable = document.getElementsByName("skuAndSize")[0];
        var aSizeShoe = sizesAvailable[sizesAvailable.length-1];
        for (var i=0; i<sizePriority.length; i++) {
            var thisSize = sizePriority[i];
            for (var j=0; j<sizesAvailable.length; j++) {
                var thisSizeShoeDiv = sizesAvailable[j];
                if (thisSizeShoeDiv.className !== "size-not-in-stock") {
                    if (extractShoeSize(thisSizeShoeDiv) === thisSize) {
                        console.log(thisSize);
                        sizesAvailable.value = thisSizeShoeDiv.value;
                        return thisSizeShoeDiv;
                    }
                }
            }
        }
        console.log("Couldn't find an available size");
        return aSizeShoe;
    }

    function extractShoeSize(shoeSizeDiv) {
        var rawShoeSize = shoeSizeDiv.innerText;
        var shoeSize = rawShoeSize.replace(/\s+/g, '');
        return shoeSize;
    }

    function addToCartSetup() {
        console.log("addToCartSetup");
        var clickAddToCart = window.setInterval(function() { addToCart() }, timeInterval);

        var addToCartDiv = document.getElementsByClassName("add-to-cart")[0];

        addToCartDiv.addEventListener("click", stopAddingToCart, false);

        function stopAddingToCart() {
            window.clearInterval(clickAddToCart);
        }
    }

    function addToCart() {
        var addToCartDiv = document.getElementsByClassName("add-to-cart")[0];

        if (isValidVariable(addToCartDiv)) {
            console.log("add to cart");
            addToCartDiv.click();
            //checkOutSetup();
        }
    }

    function checkOutSetup() {
        var clickCheckOut = window.setInterval(function () {checkOut() }, timeInterval);

        var checkOutDiv = document.getElementsByClassName("checkout-button")[0];

        checkOutDiv.addEventListener("click", stopCheckingOut, false);

        function stopCheckingOut() {
            window.clearInterval(clickCheckOut);
        }
    }

    function checkOut() {
        var checkOutDiv = document.getElementsByClassName("checkout-button")[0];
        var miniCartDiv = document.getElementsByClassName("mini-cart")[0];

        if (isValidVariable(checkOutDiv) && 
            miniCartDiv.style.display !== "none") {
            console.log("check out");
            checkOutDiv.click();
        }
    }

    function deleteAllCookies() {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i];
            var equalsPosition = cookie.indexOf("=");
            var name = equalsPosition > -1 ? cookie.substr(0, equalsPosition) : cookie;
            document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
        }
    }

    function isValidVariable(variable) {
        validVariable = false;
        if (variable !== null && variable !== undefined) {
            validVariable = true;
        }
        return validVariable;
    }
})();

