 
 $(document).ready( function() {
        $('#id_query').focusin(function() {
            if ( $('#id_query').val() == "Find" )
                $('#id_query').val('')
        });
        $('#id_project_id').change(function() {
            $('#searchForm').submit();
        });
    });

function controlButton(attribute,value,status)
{
     if (status == "ENABLE")
    {
        $(attribute).attr("disabled",false);
        $(attribute).css("background","#00386b");
        $(attribute).val(value);
    }
    else if (status == "DISABLE")
    {
        $(attribute).attr("disabled",true);
        $(attribute).css("background","#999");
        $(attribute).val("waiting");
    }
    else
        alert("false status");
}
function resetVal(itemList)
{
    $(itemList).val(null);
}


function submitForm(form,button,result)
{  
    var buttonValue = button.value;
        $.ajax({
            type: $(form).attr("method"),
            url: $(form).attr("action"),
            data: $(form).serialize(),
            dataType: "json",
            beforeSend: function() {
               controlButton("#"+button.id,buttonValue,"DISABLE");
                $(result).hide();
            },
            success: function(response,code) {
                if(response.result=="true")
                {
                    $(result).show().html('<div id="basarili"> <div class="baslik"> '+ response.message +' </div></div>');
                    if (response.redirect == null)
                    	$(form).each (function(){ this.reset(); });

                    else
                        window.location=(response.redirect);
                }
                else
                    $(result).show().html('<div id="hata"> <div class="baslik"> '+ response.message +' </div></div>');

                controlButton("#"+button.id,buttonValue,"ENABLE");
            },
            error: function(jqXHR, textStatus, errorMessage) {
                controlButton("#"+button.id,buttonValue,"ENABLE");
                $(result).show().html('<div id="hata"> <div class="baslik">'+textStatus+'</div> </div>');
            }
        });  
}

function deleteBox(id,button)
{
	var buttonValue = button.value;
    var result = confirm("Are you sure you want to delete this ticket?");
    if (result == true )
    {
    	$.ajax({
    		type: 'POST',
    		url: '/delete/ticket/',
    		data: { ticketId:id },
    		dataType: 'json',
    		beforeSend: function() {
    			controlButton("#"+button.id,buttonValue,"DISABLE");
    			alert("gidiyor");
    		},
    		success: function(response, code) {
    			if (response.result == "true" )
    				alert("deleted");
    			else
    				alert("not deleted");
    			controlButton("#"+button.id,buttonValue,"ENABLE");
    		},
            error: function(jqXHR, textStatus, errorMessage) {
    			alert("error" + textStatus + " " + errorMessage)
    		}

    	});
    }
}