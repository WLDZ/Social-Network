document.addEventListener('DOMContentLoaded', function() {


    document.querySelectorAll(".vdislike").forEach(button => {  //event listener on button class instad of a particular button
        button.onclick =function(){
    
          user_id = button.id.split("dl")[0];
        //check_like(user_id);  //current user id is being managed through django view
          
          disliked(user_id)
          
        }   
    })


    document.querySelectorAll(".vdislike").forEach(button => {  //event listener on button class instad of a particular button
        {
  
        user_id = button.id.split("dl")[0];         
        change_dislike_button_color(user_id)
  
        }   
    })

});




async function mfn8(user_id) {
  const response  = await fetch(`/check_dislike/${user_id}/`)
  const data = await response.json();
  //the addData adds the object "data" to an array
  return data
}

async function disliked(user_id) {
  
  let result =   await mfn8(user_id);
  
  if (result == true)
  {
    fetch('/dislike/', {
      method: 'POST',
      body: JSON.stringify({
      postid: user_id  
      })
      })
      .then(response => response.json())
      .then(result => {
        
      });

      likes_count = parseInt(document.getElementById(`lbd${user_id}`).innerHTML,10)
      document.getElementById(`lbd${user_id}`).innerHTML =likes_count+=1
      document.getElementById(`${user_id}dl`).style.backgroundColor = "grey" 
      
      
  
  }
  else{
    fetch('/undislike/', {
      method: 'POST',
      body: JSON.stringify({
      postid: user_id  
      })
      })
      .then(response => response.json())
      .then(result => {
      });

      likes_count = parseInt(document.getElementById(`lbd${user_id}`).innerHTML,10)
      document.getElementById(`lbd${user_id}`).innerHTML =likes_count-=1
      document.getElementById(`${user_id}dl`).style.backgroundColor = "#FF9C92"

  }


 
  
}



async function change_dislike_button_color(user_id) {
  
    let result =   await mfn8(user_id);
   
    if (result == false)
    {
  
      document.getElementById(`${user_id}dl`).style.backgroundColor = "grey" 
    }
    
  }




