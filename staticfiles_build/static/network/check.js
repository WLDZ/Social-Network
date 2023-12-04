// document.addEventListener('DOMContentLoaded', function() {

// // olike is the like button present on the view_all_posts.html
// // olike is the like button present on the view_all_posts.html
// // 

// // this file is not being used anymore

//    document.querySelectorAll(".olike, .like, .vlike").forEach(button => {  //event listener on button class instad of a particular button
//         {

//         user_id = button.id.split("l")[0];         
//         change_button_color(user_id)

//         }   
//     })
    
// });


// async function check_like(user_id) {
//   const response  = await fetch(`/check_like/${user_id}/`)
//   const data = await response.json();
//   //the addData adds the object "data" to an array
//   return data
// }

// async function change_button_color(user_id) {
  
//   let result =   await check_like(user_id);
 
//   if (result == false) // if the post not already liked by the user then like it and change to color to like.
//   {

//     document.getElementById(`${user_id}l`).style.color = "blue" 
//   }
  
// }

