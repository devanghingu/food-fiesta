/* all thing which needed to cart fucntionality */

$(document).ready(function () {
  $(".cartbutton").click(function (e) {
    var form = new FormData();

    var button = $(this);
    form.append(
      "csrfmiddlewaretoken",
      $("input[name=csrfmiddlewaretoken]").val()
    );
    form.append("rest_id", $("#rest_id").attr("data-catid"));
    form.append("food_id", $(this).attr("data-catid"));
    var abc = $.ajax({
      url: window.location.href,
      method: "POST",
      dataType: "json",
      data: form,
      processData: false,
      contentType: false,
    })
      .done(function (responce) {
        alert(responce["message"]);
        if (responce["total_item"]) {
          button.html("Added in Cart").attr("disabled", "true");
          $("#usercart").html(responce["total_item"]);
        }
      })
      .fail(function (xhr, status, errorThrown) {
        alert("" + status + " " + errorThrown);
      });
    return false;
  });

  $(".quantity").change(function (e) {
    var qty = $(this).val();
    var orditm_id = $(this).attr("id");

    //        var cart_item_id=$('#2').value();
    //        alert(cart_item_id);
    $.ajax({
      url: "../modify/quantity",
      data: {
        qty: qty,
        orditm_id: orditm_id,
      },
      dataType: "json",
      success: function (data) {
        if (data.order_id) {
          var old_price = $("#old_price").attr("value");
          var total_price = parseInt(old_price) + parseInt(data.price_adj);
          $("#price").remove();
          $("#old_price").remove();
          $(".red-bg").after(
            "<input type='text' id='old_price' value=" +
              total_price +
              " hidden='true'>"
          );
          $("#total").after(
            "<span class='price' id='price'>&#x20B9;" + total_price + "</span>"
          );
        }
      },
    });
  });
});
