document.addEventListener('DOMContentLoaded', function() {
     // NAVBAR INITIALISATION
     let navbar = document.querySelectorAll('.sidenav');
     M.Sidenav.init(navbar);

     // CAROUSEL INITIALISATION
    let carousel = document.querySelectorAll('.carousel');
    M.Carousel.init(carousel);

    // FORM SELECT INITIALISATION
    let selectInt = document.querySelectorAll('select');
    M.FormSelect.init(selectInt);


     // MODAL INITIALISATION
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


  // let message = document.getElementById("message")
  //   console.log(message)
  //   console.log("hello")

  //   setTimeout(()=>{
  //       message.fadeOut('slow')
  //     }, 2000)