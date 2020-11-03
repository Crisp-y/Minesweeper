import java.util.ArrayList;

public class testing {
    public static void main(String[] args) {
        ArrayList<Tile> list = new ArrayList<>();
        list.add(new Tile());
        list.add(new Tile());
        Tile tile = new Tile();
        list.add(tile);
        list.add(new Tile());
        System.out.println(list.size());
    }
}
