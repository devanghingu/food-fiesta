/* all thing which needed to cart fucntionality */

$(document).ready(function(){
    $('.cartbutton').click(function(e){
        var form = new FormData();
        form.append('rest_id',$('#rest_id').attr('data-catid'));
        form.append('food_id',$(this).attr('data-catid'));
        form.append('csrfmiddlewaretoken',$("input[name=csrfmiddlewaretoken]").val());
        console.log($("input[name=csrfmiddlewaretoken]").val());
        var abc= $.ajax({
            url: window.location.href,
            method: "POST",
            dataType: "json",
            data: form,
            processData: false,
            contentType:false,
        }).done(function(data){
            alert("done")
        })
        .fail(function(xhr, status, errorThrown ){
            alert(""+status+" "+errorThrown)
        });
        return false
    });
});