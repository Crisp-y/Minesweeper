public class Tile {
    Boolean mine = false;
    int nearbyMines = 0;
    Boolean clicked = false;

    public Tile(){
    }

    public Tile(int mines){
        nearbyMines = mines;
    }

    public Tile(int mines, Boolean isMine){
        nearbyMines = mines;
        mine = isMine;
    }

    public Boolean isMine() throws Exception{
        if (mine && nearbyMines == 9) {
            return true;
        }else if (!mine && nearbyMines < 9) {
            return false;
        } else {
            throw new Exception("Tile data disagrees");
        }
    }

    public void click(){
        clicked = true;
    }
}
