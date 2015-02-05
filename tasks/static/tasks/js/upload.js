$(document).ready(function()
{
    if (document.getElementById('uploadPreview')){
        def_img =  $('#uploadPreview').attr("src");
    }
});

function PreviewImage()
{
    var oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("uploadImage").files[0]);
    oFReader.onload = function (oFREvent) {
        if (oFREvent.target.result.indexOf("data:image") +1)
        {
            $('#uploadPreview').attr("src", oFREvent.target.result);
        }
        else
        {
            $('#uploadPreview').attr("src", "/static/tasks/img/no-image.png");
        }
    };
    $("#display").show();
}

function PreviewImageSelect()
{
    var selected_value = $("#id_select").val();
    if (selected_value == "")
    {
        $('#uploadPreview').attr("src", def_img);
    }
    else
    {
        $('#uploadPreview').attr("src", "/media/" + selected_value);
    }
}