import argparse
from ultralytics import YOLO
import cv2


def run_inference(input_path, output_path):
    model = YOLO('yolov8n.pt')
    # Dua kondisi untuk image dan video
    if input_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        # Pred image
        results = model.predict(input_path, conf=0.65, iou=0.7)
        for result in results:
            # Plot hasil deteksi YOLO
            detected_image = result.plot()
            # Simpan gambar
            cv2.imwrite(output_path, detected_image)
            print(f"Saving output to: {output_path}")

    elif input_path.lower().endswith(('.mp4', '.avi', '.mov')):
        # Pred Video
        vid = cv2.VideoCapture(input_path)
        # Parameter Render Video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = int(vid.get(cv2.CAP_PROP_FPS))
        frame_width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

        while vid.isOpened():
            # Read Video
            ret, frame = vid.read()
            if not ret:
                break
            # Pred Video
            results = model.predict(frame, conf=0.65, iou=0.7)
            for result in results:
                # Plot Hasil
                detected_frame = result.plot()
                # Simpan output video
                out.write(detected_frame)

        vid.release()
        out.release()
        print(f"Saving output to: {output_path}")
    else:
        print("Format File salah!. Input dalam format gambar atau video.")


if __name__ == "__main__":
    # Parsing CLI input into inference
    parser = argparse.ArgumentParser(description="YOLOv8 Inference Script")
    parser.add_argument("--input", type=str, required=True, help="Path the image or video input")
    parser.add_argument("--output", type=str, required=True, help="Path the output dir")
    args = parser.parse_args()

    # Jalankan fungsi inference
    run_inference(args.input, args.output)
