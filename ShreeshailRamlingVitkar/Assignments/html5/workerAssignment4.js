
var a=2;
function evenNumbers()
{
    a=a+2;
    postMessage(a); // postMessage() - post a message back to the HTML page.
    setTimeout("evenNumbers()",500);
    
}

evenNumbers();