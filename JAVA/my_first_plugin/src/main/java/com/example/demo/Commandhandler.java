package com.example.demo;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

public class Commandhandler implements CommandExecutor {
    @Override
    public boolean onCommand (CommandSender sender, Command command, String label, String[] args){
        if (command.getName().equalsIgnoreCase("TNT") && sender instanceof Player){
            Plugin.LOGGER.info("you summon TNT");
        return true;
    }
        else {
        Plugin.LOGGER.info("command not found");
        return false;
    }
    }
}
