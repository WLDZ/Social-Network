document.addEventListener('DOMContentLoaded', function() {


   document.querySelectorAll(".olike").forEach(button => {  //event listener on button class instad of a particular button
        {

        user_id = button.id.split("l")[0];         
        change_button_color(user_id)

        }   
    })
      //ideally there sholud be one method that take cares of all the like buttons. But, due to different technical reaseon we have two i.e olike and like

    document.querySelectorAll(".like").forEach(button => {  //event listener on button class instad of a particular button
        {

        user_id = button.id.split("l")[0];         
        change_button_color(user_id)

        }   
    })

    document.querySelectorAll(".vlike").forEach(button => {  //event listener on button class instad of a particular button
      {

      user_id = button.id.split("l")[0];         
      change_button_color(user_id)

      }   
  })

});


async function check_like(user_id) {
  const response  = await fetch(`/check_like/${user_id}/`)
  const data = await response.json();
  //the addData adds the object "data" to an array
  return data
}

async function change_button_color(user_id) {
  
  let result =   await check_like(user_id);
 
  if (result == false)
  {

    document.getElementById(`${user_id}l`).style.color = "blue" 
  }
  
}

