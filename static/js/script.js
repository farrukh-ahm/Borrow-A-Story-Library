document.addEventListener('DOMContentLoaded', function() {
     // NAVBAR INT
     let navbar = document.querySelectorAll('.sidenav');
     M.Sidenav.init(navbar);

     // Modal
     let popOp = document.querySelectorAll('.modal');
     let modal = M.Modal.init(popOp);
     let modalTrigger = document.getElementsByClassName("modal-trigger")
     let modalClose = document.getElementsByClassName("modal-close")
     modalTrigger.addEventListener("click", ()=>{
       modal.open()
     })
     for(let close of modalClose){
      close.addEventListener("click", ()=>{
         modal.close()
     })
     }
     
  });

  console.log("connected")