async function SetCache() {
  SetText("SetCache Jalan");
  let datafet = await fetch("http://127.0.0.1:8000/cache/createDataCache")
  let data = await datafet.json()
  
  SetText(data.message)

  console.log(data)
}

function GetCache() {
  console.log("GetCache jalan");
  SetText("GetCache jalan");
}

function SetText(TextSpan) {
  document.getElementById("respondDariServer").innerHTML = TextSpan
}


//respondDariServer
