function calculateDiscount(price,discount)
{
    var discounted_amount = price*discount/100;
    var real_price = price - discounted_amount;

    alert("Congrats You get RS : "+discounted_amount+ "  Discount");
    alert("Final Price is RS : "+ real_price);
}


alert("hello");
var price = prompt("Enter Price");
var discount = prompt("Enter Discount in %")

calculateDiscount(price,discount);