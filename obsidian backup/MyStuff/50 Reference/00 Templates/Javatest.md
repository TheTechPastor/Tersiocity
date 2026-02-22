



<%* if (await tp.file.exists("/Daily Notes/" + tp.date.now("YYYY-MM-DD"))) { %>
This file exists !
<%* } else { %>
<%* 
	
    let tLists =  tp.file.find_tfile("/Templates/Daily Notes")
    
%>
[[<% (await tp.file.create_new(tLists, /Daily Notes/ + tp.date.now("YYYY-MM-DD"))).basename %>]]
<%* } %>
    
<%* if (tp.frontmatter.type === "seedling") { %>
This is a seedling file !
<%* } else { %>
This is a normal file !
<%* } %>
    
<%* if (tp.file.tags.contains("#todo")) { %>
This is a todo file !
<%* } else { %>
This is a finished file !
<%* } %>

<%*
function log(msg) {
    console.log(msg);
}
%>
<%* log("Title: " + tp.file.title) %>
    
<%* tR += tp.file.content.replace(/stuff/, "things"); %>
