
  setTimeout(() => {
    document.querySelectorAll(".flash").forEach(flash => {
      flash.style.opacity = "0";
      setTimeout(() => flash.remove(), 500);
    });
  }, 3000);

  const circle=document.querySelector("#circle");
  const box=document.querySelector("#box");
  const close_box=document.querySelector("#close_box");

 

  close_box.addEventListener('click', () =>{
    box.style.display = "none";
  })

  circle.addEventListener('click', () =>{
    box.style.display = "block";
    box.style.display = "flex";
  })
