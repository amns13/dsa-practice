public class ANode {
    private int data;
    private ANode next = null;

    public ANode(int data) {
        this.data = data;
    }

    @Override
    public String toString() {
        return "ANode [data=" + data + "]";
    }

    public int getData() {
        return data;
    }

    public void setData(int data) {
        this.data = data;
    }

    public ANode getNext() {
        return next;
    }

    public void setNext(ANode next) {
        this.next = next;
    }
}
