package com.example.vick9.perkapp;

import android.app.Dialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.provider.MediaStore;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.CardView;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.facebook.AccessToken;
import com.facebook.CallbackManager;
import com.facebook.FacebookCallback;
import com.facebook.FacebookException;
import com.facebook.FacebookSdk;
import com.facebook.GraphRequest;
import com.facebook.GraphResponse;
import com.facebook.HttpMethod;
import com.facebook.share.ShareApi;
import com.facebook.share.Sharer;
import com.facebook.share.model.SharePhoto;
import com.facebook.share.model.SharePhotoContent;
import com.facebook.share.widget.ShareDialog;
import com.google.android.gms.playlog.internal.LogEvent;
import com.perk.perksdk.PerkEvent;
import com.perk.perksdk.PerkManager;

public class PostActivity extends AppCompatActivity {

    String key =   "b623ce13de3a04d8f145262253f7a4c94c64d7f3";
    String event = "037f5fc74e11847a6c37e8e55ca9251d810065ea";
    CallbackManager callbackManager;
    ShareDialog shareDialog;
    TextView nameBox,levelBox;
    CardView share;
    String name,level,message;
    EditText temptext;
    AppCompatActivity self;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_post);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);

        FacebookSdk.sdkInitialize(getApplicationContext());
        nameBox = (TextView)findViewById(R.id.post_name);
        levelBox = (TextView)findViewById(R.id.post_level);
        share = (CardView)findViewById(R.id.share_button);
        temptext = (EditText)findViewById(R.id.temp);
        temptext.setVisibility(View.GONE);
        self = this;
        PerkManager.startSession(PostActivity.this, key);
        String response = getIntent().getStringExtra("response");
        String []temp = response.split(",");
         name = temp[0];
         level = temp[1];
        message = temp[2];
        nameBox.setText(name);
        levelBox.setText(level);
        temptext.setText(message);
        toolbar.setTitle("Share" + name);
        setSupportActionBar(toolbar);

        callbackManager = CallbackManager.Factory.create();
        shareDialog = new ShareDialog(this);
        shareDialog.registerCallback(callbackManager, new FacebookCallback<Sharer.Result>() {
            @Override
            public void onSuccess(Sharer.Result result) {
                Toast.makeText(getBaseContext(),"Facebook post Shared!",Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onCancel() {
                Toast.makeText(getBaseContext(),"Facebook post Cancelled",Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onError(FacebookException error) {
                Toast.makeText(getBaseContext(),error.toString(),Toast.LENGTH_SHORT).show();
            }
        });
        share.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                if (takePictureIntent.resolveActivity(getPackageManager()) != null) {
                    startActivityForResult(takePictureIntent, 1);
                }
            }
        });



    }
    @Override
    protected void onActivityResult(final int requestCode, int resultCode, Intent data) {
        callbackManager.onActivityResult(requestCode, resultCode, data);
        if (requestCode == 1 && resultCode == RESULT_OK) {
            Bundle extras = data.getExtras();
            Bitmap imageBitmap = (Bitmap) extras.get("data");
            final Bitmap bmp = imageBitmap;




            final Dialog dialog = new Dialog(this);
            dialog.setContentView(R.layout.dialog);
            dialog.setTitle("Share Photo");

            // set the custom dialog components - text, image and button
            final EditText text = (EditText) dialog.findViewById(R.id.text);
            text.setText(message);
            ImageView image = (ImageView) dialog.findViewById(R.id.image);
            image.setImageBitmap(bmp);

            Button dialogButton = (Button) dialog.findViewById(R.id.dialogButtonOK);
            // if button is clicked, close the custom dialog
            dialogButton.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {


                    SharePhoto.Builder photoBuilder = new SharePhoto.Builder();
                    photoBuilder.setBitmap(bmp);

                    photoBuilder.setCaption(text.getText().toString());
                    final SharePhoto sharePhoto = photoBuilder.build();

                    final SharePhotoContent content = new SharePhotoContent.Builder()
                            .addPhoto(sharePhoto)
                            .build();

                    ShareApi.share(content, new FacebookCallback<Sharer.Result>() {
                        @Override
                        public void onSuccess(Sharer.Result result) {
                            SharedPreferences sharedPreferences = getApplicationContext().getSharedPreferences("myPrefs", MODE_PRIVATE);
                            String id = sharedPreferences.getString("latest","NULL");
                            sharedPreferences.edit().putString("latest",result.getPostId()).commit();
                            Toast.makeText(getBaseContext(), "Shared!", Toast.LENGTH_SHORT).show();
                            PerkManager.trackEvent(PostActivity.this, key, event, false, null);
                            Log.e("facebook",result.getPostId());

                        }

                        @Override
                        public void onCancel() {
                            Log.e("rer","sdsd");
                        }

                        @Override
                        public void onError(FacebookException error) {
                            Log.e("rer",error.getMessage());
                        }
                    });
                    dialog.dismiss();
                }
            });

            dialog.show();

        }
    }

}
