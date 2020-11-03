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

    // Returns true if this tile is a mine, false if it isn't
    public Boolean isMine() throws Exception{
        if (mine && nearbyMines == 9) {
            return true;
        }else if (!mine && nearbyMines < 9) {
            return false;
        } else {
            throw new Exception("Tile data disagrees. mine: " + mine + " nearbyMines: " + nearbyMines);
        }
    }

    public void click(){
        clicked = true;
    }

    // Sets this tile as a mine
    public void setMine(){
        mine = true;
        nearbyMines = 9;
    }

    // Change the number of nearby mines
    public void changeMines(int i){
        nearbyMines += i;
    }
}
