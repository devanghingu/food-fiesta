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
            method: "POST",
            dataType: "json",
            data: form,
            processData: false,
            contentType:false,
        }).done(function(responce){
            button.html('View in Cart');
            button.attr('disabled','true')
            alert("" + responce['message'])
        })  
        .fail(function(xhr, status, errorThrown ){
            alert("error=  "+status+" -> "+errorThrown)
        });

        return false
    });
});


$( ".abcd" ).change(function() {
    var abc= $(this).attr('value')
    alert(abc );
  });
