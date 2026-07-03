class Solution {
    public String simplifyPath(String path) {
        String[] parts = path.split("/");
        
        Stack<String> url = new Stack<>();

        for (String part: parts){
            System.out.println(part);
            if (part.equals(".") || part.equals("")){
                System.out.println("here");
            }
            else if (part.equals("..")) {
                if (!url.empty()) {
                    url.pop();
                }
            }
            else {
                url.push(part);
            }

        }

        return "/" + String.join("/", url);




    }
}