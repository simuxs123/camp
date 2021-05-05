const content=document.querySelectorAll('.prod-content');
if (content){
    content.forEach(el=>{
        if(el.textContent.length>=100){
            el.textContent=`${el.textContent.substr(0,100)}...`;
        }
    })
    // content.textContent=`${content.textContent.substr(0,100)}...`;
}