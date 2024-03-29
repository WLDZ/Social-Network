document.addEventListener('DOMContentLoaded', function() {
 
     
     document.querySelectorAll('.edit').forEach(button => {
       button.onclick =function(){
  
        post_id = button.value
        document.getElementById(post_id+'p').readOnly = false;
         button.style.display = "none"
         document.getElementById(post_id+'b').style.display = 'block';
  
       }
     })
  
  
     document.querySelectorAll(".save").forEach(button => {  //event listener on button class instad of a particular button
      button.onclick =function(){
  
  
        user_id = button.id.split("b")[0];
        post_id =user_id+'p'
        post = document.getElementById(post_id).value;
        document.getElementById(post_id).readOnly=true;
        button.style.display = "none"
        document.getElementById(user_id+'e').style.display = 'block';
        edit_post(user_id,post);  //current user id is being managed through django view
  
      }
  
      
    })
  
     follow_button_display() // mangaes user: a user should not be able to follow themselves.
     });
  
     
  
   
  
    function edit_post(post_id,post)
    {
    
        fetch('/edit_post/', {
          method: 'POST',
          body: JSON.stringify({
          post: post,
          postid: post_id    
          })
          })
          .then(response => response.json())
          .then(result => {
        
       
          });
    }
    
  
  
  async function get_user_id(){
    // gets the response from the api and put it inside a constant
    const response = await fetch('/user_id/');
    //the response have to be converted to json type file, so it can be used
    const data = await response.json();
    //the addData adds the object "data" to an array
    return data
  }
  
  
  async function follow_button_display() {
    
    let result =   await get_user_id();
  
   if (document.querySelector('#userid') !=null)
   {
    user_profie_id = document.querySelector('#userid').value ;
  
    if (user_profie_id == result)
    {
      //user should not see the follow button for their profile.
      document.querySelector('#follow-button').style.display = 'none'; 
    }
  
    else
    {
      document.querySelector('#follow-button').style.display = 'block';
    }
  
   }
    
  }