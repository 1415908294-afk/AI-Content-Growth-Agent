async function generate(){
const data={
industry:document.getElementById('industry').value,
platform:document.getElementById('platform').value,
audience:document.getElementById('audience').value,
duration:document.getElementById('duration').value
};

const res=await fetch('http://localhost:8000/generate',{
method:'POST',
headers:{'Content-Type':'application/json'},
body:JSON.stringify(data)
});

const result=await res.json();
document.getElementById('result').textContent=JSON.stringify(result,null,2);
}