
  document.addEventListener('DOMContentLoaded',()=>{
    document.querySelector('#likebtn').onclick=()=>{
      //this request a get request to server when like button is pressed
      const request=new XMLHttpRequest;
      request.open('GET','like',true);
      console.log(request);
      //when the request is receives it update the dom content according to it and disabled the button
      request.onload=()=>{
        const data = JSON.parse(request.responseText);
        if ((data.success)&&(data.content=='Like')){
          totalLike=data.Like;
          likespan=document.querySelector('#likespan');
          likespan.innerHTML=totalLike;
          likebtn=document.querySelector('#likebtn');
          likebtn.disabled = true;
          dislikebtn.disabled=true;
        }
      }
      request.send();
      return false;
    }
    document.querySelector('#dislikebtn').onclick=()=>{
      const request=new XMLHttpRequest;
      request.open('GET','dislike',true);
      request.onload=()=>{
        const data = JSON.parse(request.responseText);
        if ((data.success)&&(data.content=='Dislike')){
          totalDislike=data.Dislike;
          dislikespan=document.querySelector('#dislikespan');
          dislikespan.innerHTML=totalDislike;
          dislikebtn=document.querySelector('#dislikebtn');
          dislikebtn.disabled = true;
          likebtn.disabled=true;
        }
      }
      request.send();
      return false;
    }
  })