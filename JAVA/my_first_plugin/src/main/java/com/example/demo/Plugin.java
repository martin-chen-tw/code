package com.example.demo;

import java.util.logging.Logger;

import org.bukkit.plugin.java.JavaPlugin;

/*
 * demo java plugin
 */
public class Plugin extends JavaPlugin
{
  public  static Logger LOGGER=Logger.getLogger("demo");
  private Commandhandler commandhandler;
  public void onEnable()
  {
    LOGGER.info("demo enabled");
    commandhandler = new Commandhandler();
    getCommand("TNT").setExecutor(commandhandler);
  }

  public void onDisable()
  {
    LOGGER.info("demo disabled");
  }
}
