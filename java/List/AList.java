public class AList {
    private ANode head = null;
    
    public void push_front(int data) {
        ANode newnode = new ANode(data);
        newnode.setNext(head);
        head = newnode;
    }
    
    private ANode reverseRecursiveUtil(ANode node) {
        if (node == null) {
            return null;
        }
        
        if (node.getNext() == null) {
            head = node;
            return node;
        }
        
        ANode rest = reverseRecursiveUtil(node.getNext());
        rest.setNext(node);
        node.setNext(null);
        return node;
    }
    
    public void reverseRecursive() {
        if (head != null) {
            reverseRecursiveUtil(head);
        }
    }

    @Override
    public String toString() {
        StringBuilder listStr  = new StringBuilder();
        ANode cur = head;
        while (cur != null) {
            listStr.append(cur.getData());
            cur = cur.getNext();
            if (cur != null) {
                listStr.append(", ");
            }
        }
        return "AList [" + listStr + "]";
    }
    
    public static void main(String[] args) {
        AList list = new AList();
        list.push_front(1);
        list.push_front(2);
        list.push_front(3);
        list.push_front(4);
        
        System.out.println(list);
        list.reverseRecursive();
        System.out.println(list);
    }
}
