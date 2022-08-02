var students = [{name:"shree", percentage:50},{name:"shail",percentage:20}];


function iterateArray()
{
    students.forEach(e=>{
        console.log(e.name+"   "+e.percentage);
    })
}

function addToRandomPosition(position,data)
{
    students.splice(position,0,data);
}

function deleteFromRandomPosition(position)
{
    
}