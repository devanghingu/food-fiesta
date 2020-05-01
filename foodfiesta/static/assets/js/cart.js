/* all thing which needed to cart fucntionality */

$(document).ready(function(){
    $('.cartbutton').click(function(e){
        var form = new FormData();
        
        var button=$(this)
        form.append('csrfmiddlewaretoken',$("input[name=csrfmiddlewaretoken]").val());
        form.append('rest_id',$('#rest_id').attr('data-catid'));
        form.append('food_id',$(this).attr('data-catid'));
        var abc= $.ajax({
            url: window.location.href,
            method: "POST",dataType: "json",
            data: form,processData: false,contentType:false,
        }).done(function(responce){
            button.html('Added in Cart').attr('disabled','true')
            alert(responce['message'])
            if(responce['total_item'])
            {   $('#usercart').html(responce['total_item']); }
        })  
        .fail(function(xhr, status, errorThrown ){
            alert("error=  "+status+" -> "+errorThrown)
        });
        return false
    });
});
