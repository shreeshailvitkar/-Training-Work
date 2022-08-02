//---------------------------------  Assignment No 1 ------------------------------------------//
function oneGetMyLocation()
{
    var outputOne = document.getElementById("output-one");
    if(navigator.geolocation)
    {
        var location = navigator.geolocation.getCurrentPosition(myLocation);
        alert(location.coords.latitude);
        
    }else
    {
        outputOne.innerHTML = "Browser Not Supported";
    }
    function myLocation(position)
    {
        outputOne.innerHTML = "Latitude : "+ position.coords.latitude + "<br> Longitude : "+ position.coords.longitude;
    }
}

function oneHide()
{
    var outputOne= document.getElementById("output-one");
    outputOne.innerHTML= "";
}

//---------------------------------  Assignment No 2 ------------------------------------------//

function twoChangeColor()
{

    var selectPara = document.querySelector("p.twoPara");
    selectPara.style.color =  "red";
}


//---------------------------------  Assignment No 3 ------------------------------------------//

function allowDrop(event)
{
    
    event.preventDefault();
    //alert("1");
}

function drag(event)
{
    event.dataTransfer.setData("text", event.target.id);
    //alert("2");

}
function drop(event)
{
    event.preventDefault();
    var data = event.dataTransfer.getData("text");
    event.target.appendChild(document.getElementById(data));
    //alert("3");
}

//---------------------------------  Assignment No 4 ------------------------------------------//

var w;
function webWorker()
{
    
    if(typeof(Worker)!== "undefined")
    {
        if(typeof(w)=="undefined")
        {
            w = new Worker("workerAssignment4.js");
        }
        w.onmessage = function(event)
        {
            document.getElementById("four-output").innerHTML = " Even Numbers : " + event.data;
        }
    }else
    {
        document.getElementById("four-output").innerHTML = "Browser Not Supported";
    }
}
function stopWebWorker()
{
    w.terminate();
    w = undefined;
}


//---------------------------------  Assignment No 5 ------------------------------------------//


function myCanvas()
{
    var paper = document.getElementById('paper');
    var pen = paper.getContext('2d')
    pen.fillStyle = "yellow";
pen.beginPath();
    pen.arc(75, 75, 50, 0, Math.PI * 2, true); 
    pen.fill();
    pen.moveTo(110, 75);
    pen.arc(75, 75, 35, 0, Math.PI, false);  
    pen.moveTo(65, 65);
    pen.strokeStyle = "black";
    pen.stroke();
pen.closePath();
pen.beginPath();
    pen.fillStyle = "black";
    pen.arc(60, 65, 5, 0, Math.PI * 2, true);
    pen.fill();  
    pen.moveTo(95, 65);
    pen.arc(90, 65, 5, 0, Math.PI * 2, true);
    pen.fill();  
    pen.stroke();
}


//--------------------------------- Thank You ------------------------------------------//


