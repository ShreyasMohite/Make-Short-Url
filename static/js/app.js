const show=()=> {
    const text=document.getElementById("urls");
    navigator.clipboard.writeText(text.innerText);
}


